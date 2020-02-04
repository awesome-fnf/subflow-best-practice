# -*- coding: utf-8 -*-

import json
import random


def handler(event, context):
    evt = json.loads(event)
    if 'auditMessage' not in evt:
        return '{"result": "auditMessage not specified", "audited": false}'

    seed = random.randint(0, 10)
    if seed > 8: # not audited
        return '{"result": "audit denied with input: %s", "audited": false}' % evt['auditMessage']

    return '{"result": "audit passed", "audited": true}'

