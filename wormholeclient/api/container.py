import requests
import requests.exceptions
from .. import utils
from .. import errors


class ContainerApiMixin(object):

    def create_container(self, image_name, volume_id=None, network_info=None, block_device_info=None,
                         inject_files=None, admin_password=None, timeout=10):
        params = {'t': timeout}
        url = self._url("/container/create")
        create_config = utils.create_container_config(image_name, volume_id=volume_id, network_info=network_info,
                                                      block_device_info=block_device_info, inject_files=inject_files,
                                                      admin_password=admin_password)
        res = self._post_json(url, params=params, data=create_config)
        self._raise_for_status(res)
        return res.raw

    def restart_container(self, timeout=10, network_info=None, block_device_info=None):
        params = {'t': timeout}
        url = self._url("/container/restart")
        restart_config = utils.restart_container_config(network_info, block_device_info)
        res = self._post_json(url, params=params, data=restart_config)
        self._raise_for_status(res)
        return res.raw

    def stop_container(self, timeout=10):
        params = {'t': timeout}
        url = self._url("/container/stop")
        res = self._post_json(url, params=params, data=None)
        self._raise_for_status(res)
        return res.raw

    def start_container(self, timeout=10, network_info=None, block_device_info=None):
        params = {'t': timeout}
        url = self._url("/container/start")
        start_config = utils.start_container_config(network_info, block_device_info)
        res = self._post_json(url, params=params, data=start_config)
        self._raise_for_status(res)
        return res.raw

    def inject_files(self, inject_files, timeout=10):
        params = {'t': timeout}
        url = self._url("/container/inject-files")
        res = self._post_json(url, data={ 'inject_files' : inject_files })
        self._raise_for_status(res)
        return res.raw

    def pause_container(self, timeout=10):
        params = {'t': timeout}
        url = self._url("/container/pause")
        res = self._post_json(url, params=params, data=None)
        self._raise_for_status(res)
        return res.raw

    def unpause_container(self, timeout=10):
        params = {'t': timeout}
        url = self._url("/container/unpause")
        res = self._post_json(url, params=params, data=None)
        self._raise_for_status(res)
        return res.raw

    def get_console_output(self, timeout=10):
        params = {'t': timeout}
        url = self._url("/container/console-output")
        try:
            return self._result(self._get(url, params=params), True)
        except requests.exceptions.ConnectionError as ce:
            raise errors.ConnectionError()
        except Exception as e:
            raise errors.InternalError()

    def set_admin_password(self, admin_password, timeout=10):
        params = {'t': timeout}
        url = self._url("/container/admin-password")
        admin_password_config = utils.admin_password_config(admin_password)
        res = self._post_json(url, params=params, data=admin_password_config)
        self._raise_for_status(res)
        return res.raw

    def create_image(self, image_id, timeout=10):
        params = {'t': timeout}
        url = self._url("/container/create-image")
        create_image_config = utils.create_image_config(image_id)
        res = self._post_json(url, params=params, data=create_image_config)
        self._raise_for_status(res)
        return res.raw