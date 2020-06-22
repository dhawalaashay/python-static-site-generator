import typer
from ssg.site import Site

def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}
    # config = dict()
    # config["source"] = source
    # config["dest"] = dest

    Site(**config).build()
    # site_instance = Site(**config)
    # site_instance.build()


typer.run(main)

