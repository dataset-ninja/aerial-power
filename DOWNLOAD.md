Dataset **Aerial Power Infrastructure** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/G/s/zx/rnRveIEYOSl3Za4XjVIrLOmUKCHlPnFxIFYvXcIQfKizq7KDVVuzOUij3V2DpuqwnzL2b7OkV75d6RcScvXbpV3JywWnID2Ku6bHKRz7TADVDcS2hL2hIXXryiwq.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Aerial Power Infrastructure', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Annotations](https://zenodo.org/record/7781388/files/Annotations.zip?download=1)
- [Labels](https://zenodo.org/record/7781388/files/labels.txt?download=1)
- [Test](https://zenodo.org/record/7781388/files/Test.zip?download=1)
- [Train](https://zenodo.org/record/7781388/files/Train.zip?download=1)
- [Valid](https://zenodo.org/record/7781388/files/Valid.zip?download=1)
