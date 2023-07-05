Dataset **Aerial Power Infrastructure** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/Q/5/fn/jIZCPw9pyoZHXJBf4TwNQzF6nMBdnIPTPkVTWJK47K9qIfBuS2Dm9xzNoSBynViYYdu4MBL7fx7eYTac5shHJJVMKIEqzRSnWZoATMfnEOoVpStEYgBEzEW1K1Ee.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Aerial Power Infrastructure', dst_path='~/dtools/datasets/Aerial Power Infrastructure.tar')
```
The data in original format can be downloaded here:

- 🔗[Annotations](https://zenodo.org/record/7781388/files/Annotations.zip?download=1)
- 🔗[Labels](https://zenodo.org/record/7781388/files/labels.txt?download=1)
- 🔗[Test](https://zenodo.org/record/7781388/files/Test.zip?download=1)
- 🔗[Train](https://zenodo.org/record/7781388/files/Train.zip?download=1)
- 🔗[Valid](https://zenodo.org/record/7781388/files/Valid.zip?download=1)
