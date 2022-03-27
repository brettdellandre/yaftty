# yaftty
Yet Another File Transfer Tool, Yay! (a.k.a. yaftty) creates and manages high speed transfer from any PowerScale OneFS cluster to a VAST cluster using distributed resources which read and write of data while accurately monitoring progress, performance &amp; creating snapshots for continuous delta synchronizations.

Use Cases:
- Data Migration
- Backup/Mirror
- Archive/Offload

Reasons:
- Fast
- Monitored
- Intelligent

OneFS Requirements
- SnapshotIQ
- SmartQuotas

OneFS (Isilon/PowerScale) Arguments
--onefs-mgmt-ip
--onefs-mgmt-username
--onefs-mgmt-password
--onefs-access-zone

VAST Data Arguments
--vast-vms-ip
--vast-vms-username
--vast-vms-password
--vast-vip-pool

Reuqired Arguments
--source-path
--destination-path

Optional Arguments
--vast-alias
--threads-per-cnode

Example 
python3 ./yaftty.py --onefs-mgmt-ip 192.168.100.1 --onefs-mgmt-username root --onefs-mgmt-password "a" --onefs-access-zone "System" --vast-vms-ip 192.168.200.1 --vast-vms-username admin --vast-vms-password "123456" --vast-vip-pool "main" --source-path "/ifs/data/" --destination-path "/data/" --vast-alias "/ifs/data/"