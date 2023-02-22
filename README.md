# serverless-pipeline

## 0. Introduction

This repository contains the source code for a serverless function pipeline.

Some serverless functions use different resources in different stages. For example, a video processor first downloads a video from user or cloud storage, then processes the video, and finally uploads the result. The resource bottleneck for each stage is network download IO, CPU, and network upload IO. Therefore, we can pipeline the functions, so that one function can use network while another function is using CPU. Pipelining could increase resource utility and thus let the cluster handle more request in a given time period.

## 1. Content

- **mybench/** contains benchmark applications. These applications are provided by [SeBS](https://github.com/spcl/serverless-benchmarks) and are modified to run on Knative.

- **pipeline/** contains implementation of our pipeline. (code will be released soon).

## 2. Contact

For any question, please contact ``mashengjie at pku dot edu dot cn``.