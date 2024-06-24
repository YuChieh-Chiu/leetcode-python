import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - we need to calculate the `cancellation rate` of UNBANNED uses and drivers
    - and we know `client_id` and `driver_id` is the FK to the `user_id`
    - so, we need to follow the steps:
        (1) filter trips BETWEEN `2013-10-01` to `2013-10-03`
        (2) filter users UNBANNED (banned = No) and only get column `user_id`
        (3) filter `client_id` and `driver_id` BOTH in users
        (4) turn the value in `status` to (0,1) so that we can do calculation
        (5) groupby `request_at` and calculate COUNT(cancelled_by_driver + cancelled_by_client) / COUNT(all status)
        (6) rename to get the correct column names
    """
    trips = trips[(trips["request_at"]>="2013-10-01") & (trips["request_at"]<="2013-10-03")]
    users = users[users["banned"]=="No"].loc[:, "users_id"].to_list()
    trips = trips[(trips["client_id"].isin(users)) & (trips["driver_id"].isin(users))]
    trips["status"] =\
        trips["status"].apply(lambda x: 1 if x in ["cancelled_by_client", "cancelled_by_driver"] else 0)
    trips = trips.groupby(["request_at"])["status"].agg("mean").round(2).to_frame()
    trips.reset_index(inplace=True)
    trips.rename(
        columns={
            "request_at": "Day",
            "status": "Cancellation Rate"
        },
        inplace=True
    )
    return trips
