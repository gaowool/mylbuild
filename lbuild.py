import json

class lbuild:
    def __init__(self, context : str) -> None:
        data= json.loads(context)
        self.name=data["name"]
        self.version=data["version"]
        self.dependencies=data["dependencies"]
        self.license=data["license"]
        self.descriptions=data["descriptions"]
        self.Maintainer=data["Maintainer"]
        self.src_url=data["src_url"]
        self.src=data["src"]
        self.hash_type=data["hash"].split(" ")[0]
        self.hash=data['hash'].split(" ")[-1]
        self.pre=data['pre']
        self.Configuration=data['Configuration']
        self.make=data['make']
        self.install=data['install']
        self.post=data['post']
        pass

    def __str__(self) -> str:
        fstr=''
        fstr+=self.name+"-"+self.version+"\t"+self.license+"\n"
        fstr+="from:\t"+self.src_url+"\n"
        fstr+=self.descriptions
        return fstr
    
    def save(filename):
        data={
            "name":self.name,
            "version":self.version,
            "dependencies":self.dependencies,
            "license":self.license,
            "descriptions":self.descriptions,
            "Maintainer":self.Maintainer,
            "src_url":self.src_url,
            "src":self.src,
            "hash":" ".join([self.hash_type,self.hash]),
            "pre":self.pre,
            "Configuration":self.Configuration,
            "make":self.make,
            "install":self.install,
            "post":self.post
        }
        with open(filename,'w') as f:
            json.dump(data,f)

def lbuild_file(filename : str) -> lbuild:
    with open(filename) as f:
        context=f.read()
    return lbuild(context)
