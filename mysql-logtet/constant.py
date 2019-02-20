from enum import Enum

class StatusConstant(Enum):
    success = '成功'
    fail = '失败'

class OperationAction(Enum):
    # API操作时对应的操作常量
    CREATE = "create"
    START = "start"
    STOP = "stop"
    REBOOT = "reboot"
    SUSPEND = "suspend"

class ResourceType(Enum):
    identity = '认证'
    user = '用户'

class ComputeConstant(Enum):
    # 桌面状态相关常量
    DISCONNECT = 'DISCONNECT'
    CONNECT = 'CONNECT'
    SHUTOFF = 'SHUTOFF'
    ACTIVE = 'ACTIVE'
    RESUME = 'RESUME'
    SUSPENDED = 'SUSPENDED'
    BUILDING = 'BUILDING'
    PAUSED = 'PAUSED'
    VERIFY_RESIZE = 'VERIFY_RESIZE'
    ERROR = 'ERROR'
    HARD_REBOOT = "HARD"
    AVAILABLE = "AVAILABLE"


class ComputeAction(Enum):
    # 针对desktop做action时，传递参数与状态判断是定义的变量
    REBOOT = "reboot"
    START = "os-start"
    STOP = "os-stop"
    RESUME = "resume"
    SUSPEND = "suspend"
    DELETE = "delete"
    ATTACH_PCI = "attach-pci"
    DETACH_PCI = "detach-pci"
    ATTACH_VOLUME = "attach-volume"
    DETACH_VOLUME = "detach-volume"
    ACTIVATE = "activate"
    GET_SDAP_ADDRESS = "get_sdap_address"


class ResourceStatus(Enum):
    # 资源的状态常量
    DISABLE = 'disable'
    ENABLE = 'enable'
    ENABLED = "enabled"
    DISABLED = "disabled"
    ONLINE = "online"
    OFFLINE = "offline"


class DesktopPoolType(Enum):
    EXCLUSIVE = "exclusive"
    RESTORE = "restore"


class UserConstant(Enum):
    DEFAULT_DOMAIN = "default"


class ListResourceName(Enum):
    Desktop = "desktops"
    Image = "images"
    Flavor = "flavors"
    Pci = "pcis"
    Volume = "volumes"
    Network = "networks"


class ZstackL3NetworkType(Enum):
    L3BasicNetwork = "L3BasicNetwork"
    L3VpcNetwork = "L3VpcNetwork"


CALLBACK_URL = "http://{host}:{port}".format(host=host, port=port)
CONTENT_TYPE = 'application/json'
DEFAULT_ADMIN_UUID = "deafult_xview_admin"
ZSTACK_TYPE = "ZSTACK"
EVM_TYPE = "EVM"

ERROR_STATUS_DESKTOP_TEMPLATE = DesktopViewModel(
    uuid="",
    display_name="",
    host_name="",
    status = ComputeConstant.ERROR.value,
    enabled = "disabled",
    os_type="",
    node={"name": ""},
    flavor={
        "uuid": "",
        "vcpu": 0,
        "disk": 0,
        "ram": 0
    },
    networks=[{
        "name": "",
        "ip_addr": "",
        "mac_addr": "",
        "version": ""
    }],
    image={"uuid": "", "name": ""},
    created_at=100000,
    updated_at=100000,
    volumes_attached=[{"uuid": "", "name": "", "size": 0}],
).endict()
