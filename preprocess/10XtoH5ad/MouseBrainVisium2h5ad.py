import numpy as np
import h5py
import scanpy as sc

path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059050"
anndata1 = sc.read_visium(path,count_file='filtered_feature_bc_matrix.h5', load_images=True,
                source_image_path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059050/spatial")
anndata1.var_names_make_unique()
anndata1.write(filename="ST8059050.h5ad", compression=None, compression_opts=None, force_dense=None, as_dense=())

path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059051"
anndata1 = sc.read_visium(path,count_file='filtered_feature_bc_matrix.h5', load_images=True,
                source_image_path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059051/spatial")
anndata1.var_names_make_unique()
anndata1.write(filename="ST8059051.h5ad", compression=None, compression_opts=None, force_dense=None, as_dense=())

path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059052"
anndata1 = sc.read_visium(path,count_file='filtered_feature_bc_matrix.h5', load_images=True,
                source_image_path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059052/spatial")
anndata1.var_names_make_unique()
anndata1.write(filename="ST8059052.h5ad", compression=None, compression_opts=None, force_dense=None, as_dense=())

path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059048"
anndata1 = sc.read_visium(path,count_file='filtered_feature_bc_matrix.h5', load_images=True,
                source_image_path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059048/spatial")
anndata1.var_names_make_unique()
anndata1.write(filename="ST8059048.h5ad", compression=None, compression_opts=None, force_dense=None, as_dense=())

path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059049"
anndata1 = sc.read_visium(path,count_file='filtered_feature_bc_matrix.h5', load_images=True,
                source_image_path="/home1/zhaolianhe/SPDB/MourseBrain/mouse_brain_visium_data/mouse_brain_visium_data/rawdata/ST8059049/spatial")
anndata1.var_names_make_unique()
anndata1.write(filename="ST8059049.h5ad", compression=None, compression_opts=None, force_dense=None, as_dense=())
