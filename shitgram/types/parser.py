from json import dumps

class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __default__(obj: "Parser"):
        return {
            **{
                attr: (
                    getattr(obj, attr)
                )
                for attr in obj.__dict__
                if getattr(obj, attr) is not None and not attr.startswith("_")
            }
        } if not isinstance(obj, set) else [i for i in obj]

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Parser.__default__, ensure_ascii=False)

    def __repr__(self) -> str:
        return "\n"+dumps(self, indent=4, default=Parser.__default__, ensure_ascii=False)
