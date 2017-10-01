import json
import logging
import unittest

from render_quill import render_quill

logger = logging.getLogger(__name__)


class TestRenderQuill(unittest.TestCase):
    def test_basic(self):
        raw = "{\"ops\":[{\"insert\":\"plain \"},{\"attributes\":{\"bold\":true},\"insert\":\"bold bold \"},{\"attributes\":{\"underline\":true},\"insert\":\"underline \"},{\"attributes\":{\"underline\":true,\"italic\":true},\"insert\":\"underline-italic\"},{\"attributes\":{\"underline\":true},\"insert\":\" underline\"},{\"insert\":\" \"},{\"attributes\":{\"bold\":true},\"insert\":\"bold\"},{\"insert\":\"\\nall \"},{\"attributes\":{\"underline\":true},\"insert\":\"the styles\"},{\"insert\":\" \"},{\"attributes\":{\"underline\":true,\"bold\":true},\"insert\":\"bold-underline\"},{\"attributes\":{\"underline\":true,\"italic\":true,\"bold\":true},\"insert\":\" bold-underline-italic\"},{\"attributes\":{\"underline\":true,\"italic\":true},\"insert\":\" italic-underline\"},{\"attributes\":{\"italic\":true},\"insert\":\" italic\"},{\"insert\":\"\\nheading 1\"},{\"attributes\":{\"header\":1},\"insert\":\"\\n\"},{\"insert\":\"heading 2\"},{\"attributes\":{\"header\":2},\"insert\":\"\\n\"},{\"insert\":\"heading 3\"},{\"attributes\":{\"header\":3},\"insert\":\"\\n\"},{\"insert\":\"normal\\none\"},{\"attributes\":{\"list\":\"ordered\"},\"insert\":\"\\n\"},{\"insert\":\"two\"},{\"attributes\":{\"list\":\"ordered\"},\"insert\":\"\\n\"},{\"insert\":\"two a\"},{\"attributes\":{\"indent\":1,\"list\":\"ordered\"},\"insert\":\"\\n\"},{\"insert\":\"two b\"},{\"attributes\":{\"indent\":1,\"list\":\"ordered\"},\"insert\":\"\\n\"},{\"insert\":\"three\"},{\"attributes\":{\"list\":\"ordered\"},\"insert\":\"\\n\"},{\"insert\":\"the middle\\ndot\"},{\"attributes\":{\"list\":\"bullet\"},\"insert\":\"\\n\"},{\"insert\":\"dot dot\"},{\"attributes\":{\"list\":\"bullet\"},\"insert\":\"\\n\"},{\"insert\":\"dot dot dot\"},{\"attributes\":{\"list\":\"bullet\"},\"insert\":\"\\n\"},{\"insert\":\"the penultimate\\nsome long blocks of text, plain text on multiple lines\\nbefore\\n\"},{\"attributes\":{\"bold\":true},\"insert\":\"a long block of bold\"},{\"insert\":\"\\n\"},{\"attributes\":{\"bold\":true},\"insert\":\"text spanning\"},{\"insert\":\"\\n\"},{\"attributes\":{\"bold\":true},\"insert\":\"multiple lines\"},{\"insert\":\"\\nthe end\\n\"}]}"
        ob = json.loads(raw)
        # previous 'golden output' from running this test
        expected = '<p>plain <strong>bold bold </strong><u>underline </u><u><em>underline-italic</em></u><u> underline</u> <strong>bold</strong></p><p>all <u>the styles</u> <strong><u>bold-underline</u></strong><strong><u><em> bold-underline-italic</em></u></strong><u><em> italic-underline</em></u><em> italic</em></p><h1>heading 1</h1><h2>heading 2</h2><h3>heading 3</h3><p>normal</p><ol><li>one</li><li>two</li><ol class="ql-indent-1"><li>two a</li><li>two b</li></ol><li>three</li></ol><p>the middle</p><ul><li>dot</li><li>dot dot</li><li>dot dot dot</li></ul><p>the penultimate</p><p>some long blocks of text, plain text on multiple lines</p><p>before</p><p><strong>a long block of bold</strong></p><p><strong>text spanning</strong></p><p><strong>multiple lines</strong></p><p>the end</p>'
        # what quill.js renders the raw document above as, we're 'close enough', and visually equivalent
        target = '''<p>plain <strong>bold bold </strong><u>underline </u><em><u>underline-italic</u></em><u> underline</u> <strong>bold</strong></p><p>all <u>the styles</u> <strong><u>bold-underline</u><em><u> bold-underline-italic</u></em></strong><em><u> italic-underline</u> italic</em></p><h1>heading 1</h1><h2>heading 2</h2><h3>heading 3</h3><p>normal</p><ol><li>one</li><li>two</li><li class="ql-indent-1">two a</li><li class="ql-indent-1">two b</li><li>three</li></ol><p>the middle</p><ul><li>dot</li><li>dot dot</li><li>dot dot dot</li></ul><p>the penultimate</p><p>some long blocks of text, plain text on multiple lines</p><p>before</p><p><strong>a long block of bold</strong></p><p><strong>text spanning</strong></p><p><strong>multiple lines</strong></p><p>the end</p>'''
        out = render_quill(ob)
        if expected != out:
            logger.info(out)
        assert expected == out, (expected, out)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
