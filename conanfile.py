from conans import ConanFile


class UbitrackConan(ConanFile):
    name = "ubitrack"
    version = "1.3.0"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/Ubitrack/ubitrack.git"
    description = "Meta-Package for TUM CAMPAR Ubitrack Tracking and Sensor Fusion Framework"
    license = "GPL"

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
               "with_camera_directshow": [True, False],
               "with_camera_flycapture": [True, False],
               "with_camera_kinect2": [True, False],
            }

    default_options = (
        "shared=True",
        "with_default_camera=True",
        "with_network=True",
        "with_tracker_art=True",
        "with_vision=True",
        "with_vision_aruco=True",
        "with_visualization=True",
        #optional packages
        "with_haptic_calibration=False",
        "with_camera_directshow=False",
        "with_camera_flycapture=False",
        "with_camera_kinect2=False",
        "glad:extensions=None",
       )

    requires = (
        "ubitrack_core/[>=%s]@ubitrack/stable" % version,
        "ubitrack_component_core/[>=%s]@ubitrack/stable" % version,
        "ubitrack_dataflow/[>=%s]@ubitrack/stable" % version,
        "ubitrack_facade/[>=%s]@ubitrack/stable" % version,
        "ubitrack_virtualenv_generator/[>=%s]@ubitrack/stable" % version,
        )

    def config_options(self):
        if not self.options.with_vision:
            self.options.remove("with_default_camera")
            self.options.remove("with_default_flycapture")
            self.options.remove("with_default_directshow")

        if self.settings.os != "Windows" or not self.options.with_vision:
            self.options.remove("with_camera_kinect2")


    def requirements(self):

        if self.options.with_vision:
            self.requires("ubitrack_vision/[>=%s]@ubitrack/stable" % self.version) 
            self.requires("ubitrack_component_vision/[>=%s]@ubitrack/stable" % self.version)

            if self.options.with_vision_aruco:
                self.requires("ubitrack_component_vision_aruco/[>=%s]@ubitrack/stable" % self.version)

            if self.options.with_default_camera:
                if self.settings.os == "Macos":
                    self.requires("ubitrack_device_camera_avfoundation/[>=%s]@ubitrack/stable" % self.version)
                elif self.settings.os == "Windows":
                    self.requires("ubitrack_device_camera_msmf/[>=%s]@ubitrack/stable" % self.version)
                elif self.settings.os == "Linux":
                    self.requires("ubitrack_device_camera_v4l/[>=%s]@ubitrack/stable" % self.version)
                else:
                    self.output.warn("No default camera found for OS: %s" % self.settings.os)
            if self.settings.os == "Windows" and self.options.with_camera_directshow:
                self.requires("ubitrack_device_camera_directshow/[>=%s]@ubitrack/stable" % self.version)
            if self.settings.os == "Windows" and self.options.with_camera_kinect2:
                self.requires("ubitrack_device_camera_kinect2/[>=%s]@ubitrack/stable" % self.version)
            if self.options.with_camera_flycapture:
                self.requires("ubitrack_device_camera_flycapture/[>=%s]@ubitrack/stable" % self.version)

        if self.options.with_visualization:
            self.requires("ubitrack_visualization/[>=%s]@ubitrack/stable" % self.version)
            self.requires("ubitrack_component_visualization/[>=%s]@ubitrack/stable" % self.version)

        if self.options.with_tracker_art:
            self.requires("ubitrack_device_tracker_art/[>=%s]@ubitrack/stable" % self.version)

        if self.options.with_network:
            self.requires("ubitrack_device_comm_zmq/[>=%s]@ubitrack/stable" % self.version)

        if self.options.with_haptic_calibration:
            self.requires("ubitrack_hapticcalibration/[>=%s]@ubitrack/stable" % self.version)
            self.requires("ubitrack_component_hapticcalibration/[>=%s]@ubitrack/stable" % self.version)


