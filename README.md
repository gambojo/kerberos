# kerberos

## Variables
| Name | Description | Type | Default |
|---|---|---|---|
| krb_realm_name | The area that the server will serve. | string | "EXAMPLE.COM" |
| krb_kdc_port | Listning ports. | list | [88, 750] |
| krb_master_db_pass | DB password. | string | "password123" |
| krb_kadmin_user | Username of DB control. | string | "krbadmin" |
| krb_kadmin_pass | Userpassword of DB control. | string | "krbadmin123" |
| krb_master_packages | List of packages for installation on the master server. | list | [krb5-admin-server,<br />krb5-kdc,<br />krb5-kdc-ldap] |
| krb_replica_packages | Installing listt of packages for replica server. | list | ["krb5-kpropd"] |
| krb_client_packages | Installing listt of packages for clients. | list | ["krb5-config",<br />"krb5-user",<br />"libpam-krb5",<br />"python3-selinux"] |
| krb_kdc_service | Systemd unit name for KDC . | string | "krb5-kdc" |
| krb_kadmind_service | Unit of the Administrative Server. | string | "krb5-admin-server" |
| krb_kpropd_service | Unit name KDC Update server. | string | "krb5-kpropd" |
| krb_secure_random | Create SoftLink for device /dev/urandom. | bool | false |
| krb_conf_dir | Configuration Directory. | string | "/etc/krb5kdc" |
| krb_work_dir | Working Directory. | string | "/var/lib/krb5kdc" |
| krb_kdc_conf_path | Configuration file of the Center for Ticket Issues. | string | "{{ krb_conf_dir }}/kdc.conf" |
| krb_kadm5_acl_path | Access lists settings. | string | "{{ krb_conf_dir }}/kadm5.acl" |
| krb_kdc_db | Database. | string | "{{ krb_work_dir }}/principal" |
| krb_dict_file | Dictionary file. | string | "/usr/share/dict/words" |
| krb_admin_keytab | File with tickets. | string | "{{ krb_work_dir }}/kadm5.keytab" |
| krb_kdc_db_dump_path | File with a dump for replication. | string | "{{ krb_work_dir }}/replica_datatrans" |
| krb_kpropd_acl_path | Access lists settings to resolve replicas. | string | "{{ krb_conf_dir }}/kpropd.acl" |
| krb_ticket_max_life | Maximum ticket lifetime. | string | "10h 0m 0s" |
| krb_max_renewable_life | The maximum time during which the ticket can be extended. | string | "7d 0h 0m 0s" |
| krb_incremental_replication_db | Increnthalt Database replication. | bool | false |
| krb_replica_pull_updates_time | Time of tightening the increased database replica. | string | "2m" |
| krb_conf_path | Client configuration file. | string | "/etc/krb5.conf" |
| krb_dns_lookup_realm | Search for relevant SRV entries. | bool | false |
| krb_dns_lookup_kdc | Search for relevant SRV entries. | bool | false |
| krb_kdc_timesync | Check the time. | bool | true |
| krb_ccache_type | Type Kesh Accounts. | string | "4" |
| krb_forwardable | Allow the transfer of requests. | bool | true |
| krb_proxiable | Allow to receive sent queries. | bool | true |
| krb_rdns | Allow the search for names in the reverse viewing area. | bool | false |
| krb_ticket_lifetime | Ticket life time. | string | "24h" |
| krb_renew_lifetime | Ticket auto renewal time. | string | "7d" |
| krb_log_dir | Dir of logs. | string | "{{ krb_work_dir }}/log" |
| krb_default_log | Client logs file. | string | "{{ krb_log_dir }}/krb5libs.log" |
| krb_kdc_log | File logs of the Center for Ticket issuance. | string | "{{ krb_log_dir }}/krb5kdc.log" |
| krb_admin_log | Logi file of the administrative center. | string | "{{ krb_log_dir }}/krb5admin.log" |
| krb_encriptes | Used ciphers. | list | aes256-cts:normal<br />aes128-cts:normal<br />des3-hmac-sha1:normal<br />arcfour-hmac:normal<br />des-hmac-sha1:normal<br />des-cbc-md5:normal<br />des-cbc-crc:normal |

## The installation of only the master
```ini
[krb_master]
10.21.20.31
```
## Installation of the master and replica
```ini
[krb_master]
10.21.20.31

[krb_replica]
10.21.20.32
10.21.20.33
```
