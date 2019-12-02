''' entry point for repository class'''
#adding comment
from repository.repository import Repository
from utils.utils import Utils
if __name__ == "__main__":
    UTILS = Utils()
    CONFIG = UTILS.get_config_file('config.ini')
    OWNER = CONFIG.get('Repository', 'owner')
    REPOSITORY = CONFIG.get('Repository', 'repository_name')
    WATCHERS_COUNT1 = Repository()
    WATCHERS_COUNT1.watchers_count(owner=OWNER, repository=REPOSITORY)
