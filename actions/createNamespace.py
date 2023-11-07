from lib.okd import OkdClient

class createNamespace(OkdClient):
    def run(
            self,
            yaml,
            name,
            config_override=None):

        ret = False

        args = {}
        args['config_override'] = {}
        args['params'] = {}

        if config_override is not None:
            args['config_override'] = config_override

        if yaml is not None:
            args['yaml'] = yaml
        else:
            return (False, "yaml is a required parameter")


        # if 'body' in args:
        #     args['data'] = args['body']
        #     args.pop('body')

        v1_namespaces = self.oc().resources.get(api_version='v1', kind='Project')

        v1_namespaces.create(body=args['body'], namespace=args['name'])
