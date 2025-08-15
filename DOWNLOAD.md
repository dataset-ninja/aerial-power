Dataset **Aerial Power Infrastructure** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTY1Ml9BZXJpYWwgUG93ZXIgSW5mcmFzdHJ1Y3R1cmUvYWVyaWFsLXBvd2VyLWluZnJhc3RydWN0dXJlLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIkdKV1B2TzZwVWVURTIzUHhrV2dEcmIyVHh4WW9DQmVUN3RQb1FxY25nSFk9In0=?response-content-disposition=attachment%3B%20filename%3D%22aerial-power-infrastructure-DatasetNinja.tar%22)

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
