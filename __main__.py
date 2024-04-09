import os
import pulumi
import pulumi_snowflake as snowflake 

def create_snowflake_provider():
    # Create Snowflake resource provider
    snowflake_account = os.environ.get("SNOWFLAKE_ACCOUNT")
    snowflake_username = os.environ.get("SNOWFLAKE_USERNAME")
    snowflake_password = os.environ.get("SNOWFLAKE_PASSWORD")

    return snowflake.Provider("snowflake-provider", 
                              account=snowflake_account,
                              username=snowflake_username, 
                              password=snowflake_password
                              )

def create_snowflake_database(provider):
    # Create a Snowflake database
    return snowflake.Database("my_database",
                               name="MY_DATABASE",
                               opts=pulumi.ResourceOptions(provider=provider))

def create_snowflake_warehouse(provider):
    # Create a Snowflake warehouse
    return snowflake.Warehouse("my_warehouse",
                      name="MY_WAREHOUSE",
                      warehouse_size="Small",
                      auto_suspend=600,
                      auto_resume=True,
                      opts=pulumi.ResourceOptions(provider=provider))

def create_snowflake_user():
    # Create a Snowflake user
    return snowflake.User("SampleUser111",
                          login_name="SampleUser222",
                          default_role="SYSADMIN",  
                          disabled=False,           
                          first_name="John",
                          last_name="Doe",
                          email="john.doe@example.com",
                          password="V3ryStr0ngP4ssW0rd")

if __name__ == "__main__":
    provider = create_snowflake_provider()
    database = create_snowflake_database(provider)
    warehouse = create_snowflake_warehouse(provider)
    user = create_snowflake_user()








