system_telemetry = [
("srv_01", 12.5, 64, "online"),
("srv_02", 85.0, 92, "online"),
("srv_03", 0.0, 0, "offline"),
("srv_04", 45.2, 78, "online"),
("srv_05", 95.1, 99, "online")
]
#unpacking and filtering tuples
active_nodes_data = [
    (node_name, cpu_load, ram_usage)
    for node_name, cpu_load, ram_usage, status in system_telemetry
    if status == "online"
]
#forming name list
active_node_names = [name for name, _, _ in active_nodes_data]
print(f"Активные узлы в сети: {active_node_names}")
#metrics calculation using built-in aggregate function
active_nodes_count = len(active_nodes_data)
#calculating metrics with no manual increments
cpu_values = [cpu for _, cpu, _ in active_nodes_data]
ram_values = [ram for _, _, ram in active_nodes_data]
average_cpu = ( 0.0 if active_nodes_count == 0
                else round( sum(cpu_values) / active_nodes_count, 2 ) )
max_ram = max(ram_values) if ram_values else 0
#Creating nested dictionary
telemetry_report = {
    'active_nodes_count': active_nodes_count,
    'metrics': {
        'average_cpu': average_cpu,
        'max_ram': max_ram
    }
}
print("Итоговый отчет телеметрии:")
print(telemetry_report)