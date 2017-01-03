import random
import requests
import logging
from Legobot.Lego import Lego
from pyquery import PyQuery
from urllib.parse import urlencode, urljoin


logger = logging.getLogger(__name__)


class Devopsy(Lego):

    def listening_for(self, message):
        return message['text'].split()[0] == '!devopsy'

    def handle(self, message):
        logger.info(message)
        try:
            target = message['metadata']['source_channel']
            self.opts = {'target': target}
            self.message = message
        except IndexError:
            logger.error('Could not identify message source in message: {0!s}'
                         .format(str(message)))
        args = self.devopsy(message['text'].split())
        self.reply(message, args, self.opts)

    def devopsy(self, *args):
        """Return a gif based on search of several *reactions
        Ported to Legobot from:
            "https://github.com/ricardokirkner/err-devops-reactions"
            ... and extended.

        Return a random gif if no query is specified or query not found

        Example:
            !devopsy somefoofulquery
            !devopsy
        """

        base = {
                'dev': 'https://devopsreactions.tumblr.com/',
                'qa': 'https://qareacts.tumblr.com/',
                'sec': 'https://securityreactions.tumblr.com/',
                'dba': 'http://dbareactions.com/'
               }

        items = list(base.items())
        key, val = random.choice(items)  # nosec
        args = ' '.join(self.message['text'].split()[1:])
        if args and 'dev' in key:
            q = urlencode({'q': args})
            path = ''.join(['?', q])
        else:
            path = 'random'
        url = urljoin(val, path)
        r = requests.get(url)
        logger.debug('url sent: {}'.format(r.url))

        if r.ok:
            dom = PyQuery(r.content)
            results = dom('div[class=post_title] a')
            logger.debug('results found: {}'.format(len(results)))
        else:
            results = []

        if results:
            item = random.choice(results)  # nosec
            img = item.get('href')
            response = img
        else:
            path = 'random'
            noway = urljoin(url, path)
            response = 'Foo for you: {}'.format(noway)
        return response

    def get_name(self):
        return 'devopsy'

    def get_help(self):
        help_text = "Enter a query or we'll pick a random one " \
                 "Usage: !devopsy foofulquery"
        return help_text
