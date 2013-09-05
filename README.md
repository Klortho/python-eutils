eutils
======

The eutils package contains wrapper functions for calling eutils. So far, it contains esearch and esummary. To use esearch:

```python
import eutils
id = eutils.esearch("sra", term)
```

esummary takes a single id (multiple ids are not yet supported) and returns an
object of class DocumentSummary, which has an attribute, xml, containing a parsed
tree (an object of class XML from lxml).

```python
import eutils
summary = eutils.esummary("sra", id)
parsed_tree = summary.xml
```

If no document is found, a NoSummaryFoundException is raised.

Additional modules exist that extend the esummary functionality to add data.

sra:

```python
from eutils import sra
summary = sra.esummary(id)
title = summary.title
```

biosample:

```python
from eutils import biosample
summary = biosample.esummary(id)
sra = summary.sra
sample_name = summary.sample_name
```

bioproject:

```python
from eutils import bioproject
summary = bioproject.esummary(id)
organism = summary.organism
project_data_type = summary.project_data_type
```
