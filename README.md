# SEBench
A systematic evaluation of SE analysis methods with spatially resolved transcriptomics data

Here we propose to establish a systematic comparison study of SE analysis methods for all mainstream SRT data types. We will benchmark 18 SE analysis methods on a variety of publicly available datasets. Our benchmark datasets contain three parts, (1) the first part consists of the union of datasets which have been widely used by existing benchmarked methods (e.g., ST, Visium, Slide-seq, Slide-seqV2, HDST, seqFISH, seqFISH+, MERFISH), (2) the second part consists of those datasets that are less frequently used while also very important (e.g., osmFISH, and STARmap), and (3) the third part consists of recently published SRT technologies which has not been tested by any benchmarked method (e.g., the stereo-seq dataset with large FOV and nanometer spatial resolution50, seq-scope dataset with tissue level FOV and single cell spatial resolution, and EASI-FISH dataset with 3D spatial dimensionality). 

| **Method**         | **Principle**        | **Website**                                                  | **Language** |
| ------------------ | -------------------- | ------------------------------------------------------------ | ------------ |
| Trendseek          | Statistical Testing  | https://github.com/edsgard/trendsceek                        | R            |
| SpatialDE          | Statistical  Testing | https://github.com/Teichlab/SpatialDE                        | Python       |
| SPARK              | Statistical  Testing | https://github.com/xzhoulab/SPARK                            | R            |
| Gpcounts           | Statistical  Testing | https://github.com/ManchesterBioinference/GPcounts           | Python       |
| singleCellHaystack | Scoring              | https://github.com/   alexisvdb/singleCellHaystack           | R            |
| Sepal              | Scoring              | [https://github.com/almaan/sepal   ](https://github.com/almaan/sepal) | Python       |
| Binspect           | Statistical Testing  | [https://rubd.github.io/Giotto_site/.](https://rubd.github.io/Giotto_site/) | R            |
| Hotspot            | Statistical Testing  | http://www.github.com/yoseflflab/hotspot                     | Python       |
| MERINGUE           | Statistical Testing  | https://github.com/JEFworks-Lab/MERINGUE                     | R            |
| SPARK-X            | Statistical Testing  | http://www.xzlab.org/software.html                           | R            |
| SOMDE              | Statistical Testing  | https://github.com/XuegongLab/somde                          | Python       |
| SpaGCN             | Statistical  Testing | https://github.com/jianhuupenn/SpaGCN                        | Python       |
| MULTILAYER         | Scoring              | https://github.com/SysFate/MULTILAYER                        | Python       |
| SpatialDE2         | Statistical Testing  | https://github.com/PMBio/SpatialDE                           | Python       |
| BOOST-GP           | Statistical Testing  | https://github.com/Minzhe/BOOST-GP                           | R            |
| Squidpy            | Scoring              | https://github.com/theislab/squidpy                          | Python       |
| HRG                | Scoring              | http://lifeome.net/software/hrg                              | R            |
| SPRI               | Statistical Testing  | https://github.com/xiaoyeye/SPRI                             | Python       |

| **Methods**        | **NGS-based  SRT** |               |             |      |           |            |         | **Imaging-based  SRT** |         |           |         |      |
| ------------------ | ------------------ | ---------------------- | ----------- | ---- | --------- | ---------- | ------- | ------- | ------- | --------- | ------- | ---- |
|                    | ST                 | Visium             | Slide-seq              | Slide-seqV2 | HDST | Seq-scope | Stereo-seq | SeqFISH | MERFISH | osmFISH | EASI-FISH | STARmap |      |
| Trendseek          | √                  |                        |             |      |           |            |         | √       |         |           |         |      |
| SpatialDE          | √                  |                        |             |      |           |            |         | √       | √       |           |         |      |
| SPARK              | √                  |                        |             |      |           |            |         | √       | √       |           |         |      |
| Gpcounts           | √                  |                        |             |      |           |            |         |         |         |           |         |      |
| singleCellHaystack |                    | √                      |             |      |           |            |         |         |         |           |         |      |
| Sepal              | √                  | √                      | √           |      |           |            |         |         |         |           |         |      |
| Binspect           |                    | √                      | √           |      |           |            |         | √       | √       | √         |         | √    |
| Hotspot            |                    | √                      | √           |      |           |            |         |         |         |           |         |      |
| MERINGUE           |                    | √                      | √           |      |           |            |         |         | √       |           |         |      |
| SPARK-X            |                    | √                      | √           | √    | √         |            |         |         |         |           |         |      |
| SOMDE              |                    | √                      | √           |      |           |            |         |         |         |           |         |      |
| SpaGCN             | √                  | √                      |             | √    |           |            |         |         | √       |           |         | √    |
| MULTILAYER         | √                  | √                      | √           |      |           |            |         |         |         |           |         |      |
| SpatialDE2         |                    | √                      |             |      |           |            |         |         |         |           |         |      |
| BOOST-GP           |                    | √                      |             |      |           |            |         | √       | √       |           |         |      |
| Squidpy            |                    | √                      |             | √    |           |            |         | √       | √       |           |         |      |
| HRG                |                    | √                      |             |      |           |            |         |         |         |           |         |      |
| SPRI               | √                  |                        |             |      |           |            |         |         |         |           |         |      |
| SEBench            | √                  | √                      | √           | √    | √         | √          | √       | √       | √       | √         | √       | √    |
