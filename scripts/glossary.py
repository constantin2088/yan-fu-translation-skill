"""Find incompatible equivalents within a declared semantic context."""
def conflicts(entries):
 table={}
 for e in entries:
  if not isinstance(e,dict):raise ValueError('entry must be an object')
  for k in ('source','context','target'):
   if not isinstance(e.get(k),str) or not e[k].strip():raise ValueError('source context target required')
  key=(e['source'].strip(),e['context'].strip())
  table.setdefault(key,set()).add(e['target'].strip())
 return [{'source':s,'context':c,'targets':sorted(v)} for (s,c),v in sorted(table.items()) if len(v)>1]
