import paramiko
from openpyxl import Workbook
import re

ip_list = ['10.17.0.122',	'10.17.0.130',	'10.17.0.218',	'10.17.0.226',	'10.17.0.50',	'10.17.0.58',	'10.17.0.74',	'10.17.0.82',	'10.17.0.10',	'10.17.0.98',	'10.19.2.178',	'10.19.2.242',	'10.19.2.90',	'10.19.2.10',	'10.21.224.154',	'10.21.224.186',	'10.16.64.154',	'10.16.64.202',	'10.21.225.162',	'10.22.128.58',	'10.22.128.194',	'10.22.128.202',	'10.22.128.226',	'10.54.65.162',	'10.54.66.98',	'10.54.64.194',	'10.23.0.130',	'10.23.1.42',	'10.23.0.202',	'10.61.2.90',	'10.23.2.194',	'10.23.3.50',	'10.61.2.58',	'10.61.2.218',	'10.61.0.250',	'10.61.0.42',	'10.61.0.50',	'10.61.3.114',	'10.61.0.74',	'10.61.0.90',	'10.21.64.170',	'10.21.66.130',	'10.21.66.106',	'10.21.65.50',	'10.21.65.226',	'10.57.131.66',	'10.57.128.234',	'10.53.0.18',	'10.49.224.154',	'10.16.0.122',	'10.16.0.130',	'10.16.0.146',	'10.16.3.138',	'10.34.230.146',	'10.34.231.66',	'10.3.0.18',	'10.3.1.26',	'10.34.230.242',	'10.3.3.114',	'10.13.7.114',	'10.34.5.146',	'10.34.0.210',	'10.34.6.90',	'10.34.1.250',	'10.34.1.58',	'10.2.33.178',	'10.34.5.66',	'10.2.38.218',	'10.34.5.10',	'10.34.0.10',	'10.2.36.34',	'10.57.128.50',	'10.57.129.114',	'10.57.131.34',	'10.1.231.10',	'10.1.228.66',]
username = "admin"
password = "adminpsn123"

wb = Workbook()
ws = wb.active
ws.title = "Router Data"
headers = ["Router", "Ap1 To-address", "Ap1 Dst-address", "Ap2 To-address", "Ap2 Dst-address", "Error"]
ws.append(headers)

for ip in ip_list:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    row_data = [ip]
    try:
        ssh.connect(ip, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command('/ip firewall nat print')
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')

        if error:
            print(f"Error for {ip}: {error}")
            row_data.extend([""] * 4)
            row_data.append(error.strip())
        else:
            print(f"NAT Rules for {ip}:")

            to_addresses = []
            dst_addresses = []

            to_address_matches = re.findall(r'to-addresses=([\d.]+)', output)
            dst_address_matches = re.findall(r'dst-address=([\d.]+)', output)

            to_addresses.extend(to_address_matches)
            dst_addresses.extend(dst_address_matches)

            row_data.extend(to_addresses[:2] + [""] * (2 - len(to_addresses)))
            row_data.extend(dst_addresses[:2] + [""] * (2 - len(dst_addresses)))
            row_data.append("")

    except Exception as e:
        print(f"Error connecting to {ip}: {e}")
        row_data.extend([""] * 4)
        row_data.append(str(e))
    finally:
        ssh.close()

    ws.append(row_data)

wb.save("Output_1.xlsx")
print("Data has been saved to Output.xlsx")
