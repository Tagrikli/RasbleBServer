import requests
from loguru import logger
from .consts import SUCC_MSG,ERROR_MSG,API,INFO_MSG
from .helpers import getEndpoint,extractDeviceMAC

def cb_agent_registered():
    logger.info(SUCC_MSG.AGENT_REG)

def cb_agent_registered_err(err):
    logger.error(ERROR_MSG.AGENT_REG, err)

def cb_agent_unregistered():
    logger.info(SUCC_MSG.AGENT_UNREG)

def cb_agent_unregistered_err(err):
    logger.error(ERROR_MSG.AGENT_UNREG, err)

def cb_passkey(device,passkey):
    mac = extractDeviceMAC(device)
    
    logger.info(INFO_MSG.NEW_PAIR + f' {mac} -> {passkey}')
    params = {
        'mac':mac,
        'passkey':passkey
    }
    requests.get(getEndpoint(API.PASSKEY), params=params, timeout=2)
