The authors of the **Aerial Power Infrastructure Detection Dataset** explore the application of Unmanned Aerial Vehicles (UAVs) in autonomously inspecting power networks. They acknowledge the rapid progress in UAV technology and emphasize the need for efficient data acquisition in order to navigate power networks and acquire high-resolution data safely and swiftly. The dataset aims to aid the research community in training online detection models, thereby assisting UAV localization within the network.

The dataset contains top-view images of Medium Voltage (MV) poles captured across various locations in Cyprus. The images encompass different seasons, background conditions, and heights to ensure versatility. Annotations were converted into formats suitable for various frameworks. The dataset aids the detection of objects known as "t-bars," which represent poles.

Their specific focus is on the "Pole Detection" process within the ICARUS toolkit. The ICARUS is a UAV-based platform that combines UAV technology and deep learning algorithms to automate power infrastructure inspection, including data acquisition and analysis. The system employs multiple sensors and advanced navigation techniques to minimize errors and accurately identify poles. The UAV employs known pole coordinates and detects poles using a one-class detection model, correcting its position to align directly above the pole for accurate inspection.

Authors utilize commercially available UAV equipment such as DJI Matrice 300 RTK, equipped with cameras and multispectral sensors. The NVIDIA Jetson Xavier NX embedded platform enables real-time deep learning and navigation algorithms.

<img src="https://github.com/supervisely/supervisely/assets/78355358/86d057f7-6a8c-4cba-ba82-64ec2b0a9ce3" alt="image" width="400">

In the inspection procedure, the UAV autonomously takes off, navigates a predefined path, collects data, and returns to the starting point. Pole locations can be supplied with a certain tolerance. The "Pole Detection" task involves using tiny-You-Only-Look-Once (tiny-YOLO) v4 to identify poles in top-view images from various conditions and seasons.

The authors' work seeks to enhance the efficiency and accuracy of power network inspection through UAV technology, deep learning, and advanced data acquisition techniques.
