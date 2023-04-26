Edit : This repository was imported from GitLab. This is a forked repository that adapts the basic functionality of pyVHR, to the expectations of my 2021 internship. For more explanation on what pyVHR is: https://github.com/phuselab/pyVHR.

# pyvhr_v2

From the root folder, run: python -m main.py video_filename video_extension

Example: python -m main.py face mp4

The video file must be located in the sampleDataset folder

First, pyVHR saves the video with the extracted face, as a .npz in the cropped folder.
This operation is long (~5 minutes for a duration of 10 seconds).

Then pyVHR is applied to the recorded video in the cropped folder, which doesn't take much time (5~10 seconds).
A tab opens on the default browser with the iPPG graph and the graph is saved as .csv in the csv folder.

To compare 2 graphs, run the python command compare.py csv_filename1 csv_filename2 (without extensions).
