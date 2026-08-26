db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}
#getting host&port values
conn_settings = db_config["connection"]
host_value = conn_settings.get("host")
port_value = conn_settings.get("port")
#safe checking ssl_settings and ssl_mode
ssl_mode = (
    db_config
    .get("ssl_settings", {}) #returns empty dictionary if there's no key
    .get("ssl_mode", "verify-full")
)
#changing user parameter
conn_settings["user"] = "admin"
#adding max_connections parameter
conn_settings["max_connections"] = 100
#printing
print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")
for key, value in conn_settings.items():
    print(f"* {key}: {value}")