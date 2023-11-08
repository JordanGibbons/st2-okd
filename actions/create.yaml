import json
from lib.okd import OkdClient

class create(OkdClient):
    def run(
            self,
            apiVersion,
            kind,
            namespace,
            manifest,
            config_override=None):

        ret = False

        args = {}
        args['config_override'] = {}
        args['params'] = {}

        if config_override is not None:
            args['config_override'] = config_override

        if apiVersion is not None:
            args['apiVersion'] = apiVersion
        else:
            return (False, "apiVersion is a required parameter")

        if kind is not None:
            args['kind'] = kind
        else:
            return (False, "kind is a required parameter")

        if manifest is not None:
            args['body'] = manifest
        else:
            return (False, "manifest is a required parameter")

        if namespace is not None:
            args['namespace'] = namespace
        else:
            return (False, "namespace is a required parameter")


        # if 'body' in args:
        #     args['data'] = args['body']
        #     args.pop('body')

        v1_namespaces = self.oc().resources.get(api_version=args['apiVersion'], kind=args['kind'])
        print("creating  " + args['kind'] + ": " + args['name'])
        v1_namespaces.create(body=args['body'], namespace=args['namespace'])
        print("Done.")
