import sys
from lxml import etree
schema=etree.XMLSchema(etree.parse(__file__.rsplit('/',1)[0]+'/xsd/fa3-local.xsd'))
for f in sys.argv[1:]:
    ok=schema.validate(etree.parse(f)); print(f,'VALID' if ok else 'INVALID')
    for e in schema.error_log: print('  ',e.line,e.message)
