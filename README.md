# SEBench
A benchmark study on a group of methods to perform spatially variable gene selection

### How to use git lfs
Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.

#### install
```
sudo apt-get install git-lfs
```



#### config git lfs
```
cd SEBench
git lfs install
```

#### track file
```
# track some files
git lfs track "*.svg"
git lfs track "*.h5ad"
git lfs track "*.png"
# track one file
git lfs track "2.png"
git lfs track "example.lfs"
```


#### untrack file
```
git lfs untrack "*.png"
```

#### save and commit all config
```
git add .gitattributes
git commit -m "add .gitattributes"
```

#### cancel the global configuration of LFS
```
git lfs uninstall
```