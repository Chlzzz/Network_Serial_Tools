import socket

def get_local_ip():
    local_ips = ["127.0.0.1"]
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        local_ips.append(ip)
    
    local_ips.sort(reverse = True)
    return local_ips

def decode_data(bytes_arr: bytes) -> str:
    """
    :param bytes_arr: 字节数组
    :return: 字符串
    """
    try:
        msg = bytes_arr.decode("UTF-8")
    except Exception as e:
        msg = bytes_arr.decode("GBK")
    return msg