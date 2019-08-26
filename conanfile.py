from conans import ConanFile


class UbitrackConan(ConanFile):
    name = "ubitrack"
    version = "1.3.0"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/Ubitrack/ubitrack.git"
    description = "Meta-Package for TUM CAMPAR Ubitrack Tracking and Sensor Fusion Framework"
    license = "GPL"
    generators = "ubitrack_virtualenv_generator"

    options = {"shared": [True, False],
               "with_default_camera": [True, False],
               "with_network": [True, False],
               "with_haptic_calibration": [True, False],
               "with_tracker_art": [True, False],
               # disabling vision completely requires more dynamic dependency management 
               # in utdataflow/utfacade and deps..
               "with_vision": [True, False],
               "with_vision_aruco": [True, False],
               "with_visualization": [True, False],
               "with_python": [True, False],
               "with_trackman": [True, False],
               "with_camera_directshow": [True, False],
               "with_camera_flycapture": [True, False],
               "with_camera_kinect2": [True, False],
               "with_camera_zed": [True, False],
               "with_camera_realsense": [True, False],
               "with_device_videostream": [True, False],
               "with_tracker_vicon": [True, False],
               "workspaceBuild" : [True, False],
            }

    default_options = {
        "shared":True,
        "with_default_camera" : True,
        "with_network" : True,
        "with_tracker_art" : True,
        "with_vision" : True,
        "with_vision_aruco" : True,
        "with_visualization" : True,
        #optional packages
        "with_python" : False,
        "with_trackman" : False,
        "with_haptic_calibration" : False,
        "with_camera_directshow" : False,
        "with_camera_flycapture" : False,
        "with_camera_kinect2" : False,
        "with_camera_zed" : False,
        "with_camera_realsense" : False,
        "with_device_videostream" : False,
        "with_tracker_vicon" : False,
        "glad:extensions" : None,
        "workspaceBuild" : False,
       }


    def config_options(self):
        if not self.options.with_vision:
            self.options.remove("with_default_camera")
            self.options.remove("with_default_flycapture")
            self.options.remove("with_default_directshow")
            self.options.remove("with_default_realsense")
            self.options.remove("with_default_zed")

        if self.settings.os != "Windows" or not self.options.with_vision:
            self.options.remove("with_camera_kinect2")

    def requirements(self):
        userChannel = "ubitrack/stable"
        if self.options.workspaceBuild:
            userChannel = "local/dev"


        self.requires("ubitrack_core/%s@%s" % (self.version, userChannel))
        self.requires("ubitrack_component_core/%s@%s" % (self.version, userChannel))
        self.requires("ubitrack_dataflow/%s@%s" % (self.version, userChannel) )
        self.requires("ubitrack_facade/%s@%s" % (self.version, userChannel) )
        self.requires("ubitrack_virtualenv_generator/[>=%s]@ubitrack/stable" % self.version)

        if self.options.with_vision:
            self.requires("ubitrack_vision/[>=%s]@%s" % (self.version, userChannel)) 
            self.requires("ubitrack_component_vision/[>=%s]@%s" % (self.version, userChannel))

            if self.options.with_vision_aruco:
                self.requires("ubitrack_component_vision_aruco/[>=%s]@%s" % (self.version, userChannel))

            if self.options.with_default_camera:
                if self.settings.os == "Macos":
                    self.requires("ubitrack_device_camera_avfoundation/[>=%s]@%s" % (self.version, userChannel))
                elif self.settings.os == "Windows":
                    self.requires("ubitrack_device_camera_msmf/[>=%s]@%s" % (self.version, userChannel))
                elif self.settings.os == "Linux":
                    self.requires("ubitrack_device_camera_v4l/[>=%s]@%s" % (self.version, userChannel))
                else:
                    self.output.warn("No default camera found for OS: %s" % self.settings.os)

            if self.settings.os == "Windows" and self.options.with_camera_directshow:
                self.requires("ubitrack_device_camera_directshow/[>=%s]@%s" % (self.version, userChannel))

            if self.settings.os == "Windows" and self.options.with_camera_kinect2:
                self.requires("ubitrack_device_camera_kinect2/[>=%s]@%s" % (self.version, userChannel))

            if self.options.with_camera_flycapture:
                self.requires("ubitrack_device_camera_flycapture/[>=%s]@%s" % (self.version, userChannel))

            if self.options.with_camera_realsense:
                self.requires("ubitrack_device_camera_realsense/[>=%s]@%s" % (self.version, userChannel))

            if self.options.with_camera_zed:
                self.requires("ubitrack_device_camera_zed/[>=%s]@%s" % (self.version, userChannel))

            if self.options.with_device_videostream:
                self.requires("ubitrack_device_comm_videostream/[>=%s]@%s" % (self.version, userChannel))

        if self.options.with_visualization:
            self.requires("ubitrack_visualization/[>=%s]@%s" % (self.version, userChannel))
            self.requires("ubitrack_component_visualization/[>=%s]@%s" % (self.version, userChannel))

        if self.options.with_tracker_art:
            self.requires("ubitrack_device_tracker_art/[>=%s]@%s" % (self.version, userChannel))

        #if self.options.with_tracker_vicon:
        self.requires("ubitrack_device_tracker_vicon/[>=%s]@%s" % (self.version, userChannel))

        if self.options.with_network:
            self.requires("ubitrack_device_comm_zmq/[>=%s]@%s" % (self.version, userChannel))

        if self.options.with_python:
            self.requires("ubitrack_lang_python/[>=%s]@%s" % (self.version, userChannel))

        if self.options.with_haptic_calibration:
            self.requires("ubitrack_hapticcalibration/[>=%s]@%s" % (self.version, userChannel))
            self.requires("ubitrack_component_hapticcalibration/[>=%s]@%s" % (self.version, userChannel))

        if self.options.with_trackman:
            self.requires("ubitrack_tools_trackman/[>=1.0]@ubitrack/stable")


