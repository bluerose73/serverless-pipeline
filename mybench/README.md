# SeBS on knative

This folder contains benchmark applications. These applications are provided by [SeBS](https://github.com/spcl/serverless-benchmarks) and are modified to run on Knative.

The following are the applications and their resource using patterns.

| Type       | Benchmark             | Stages                        | Description                                                  |
| ---------- | --------------------- | ----------------------------- | ------------------------------------------------------------ |
| Webapps    | 120.uploader          | download, upload              | Uploader file from provided URL to cloud storage.            |
| Multimedia | 210.thumbnailer       | download, computation, upload | Generate a thumbnail of an image.                            |
| Multimedia | 220.video-processing  | download, computation, upload | Add a watermark and generate gif of a video file.            |
| Utilities  | 311.compression       | download, computation, upload | Create a .zip file for a group of files in storage and return to user to download. |
| Utilities  | 504.dna-visualization | download, computation         | Creates a visualization data for DNA sequence.               |
| Inference  | 411.image-recognition | download, computation         | Image recognition with ResNet and pytorch.                   |
