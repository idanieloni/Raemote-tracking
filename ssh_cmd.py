
import paramiko


def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    # client can also support using key files
    # client.load_host_keys('/home/user/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return

if __name__ == '__main__':
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()
    ip = input('Enter server IP: ') 
    port = input('Enter port or <CR>: ')
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)