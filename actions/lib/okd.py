from kubernetes import client
from openshift.dynamic import DynamicClient
from openshift.helper.userpassauth import OCPLoginConfiguration
from st2common.runners.base_action import Action


class OkdClient(Action):


    def __init__(self, config=None):

        super(OkdClient, self).__init__(config=config)

        self.myconfig = self.config
        self.yaml = None


    def oc(self, **args):

        if "config_override" in args:
            self.overwriteConfig(args['config_override'])
            del(args['config_override'])


        apihost = self.myconfig['api_url']
        token = self.myconfig['bearer_token']

        print(token)

        kubeConfig = client.configuration
        kubeConfig.api_key = {"authorization": "Bearer " + token})

        print("")
        print(kubeConfig.api_key)
        print("")
        kubeConfig.host = apihost
        kubeConfig.verify_ssl = True

        if 'yaml' in args:
            # yaml_object = yaml.safe_load(args['yaml'])

            # args['body'] = json.dump(yaml_object)
            args['body'] = args['yaml']


    # # Retrieve the auth token
    # kubeConfig.get_token()

    # print('Auth token: {0}'.format(kubeConfig.api_key))
    # print('Token expires: {0}'.format(kubeConfig.api_key_expires))

        k8s_client = client.ApiClient(kubeConfig)

        dyn_client = DynamicClient(k8s_client)

        return dyn_client
        # v1_projects = dyn_client.resources.get(api_version='project.openshift.io/v1', kind='Project')
        # project_list = v1_projects.get()
    def overwriteConfig(self, newconf):

        for key in newconf:
            self.myconfig[key] = newconf[key]

    # def oc(self):
