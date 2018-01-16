from conans import ConanFile


class BoostConan(ConanFile):
    name = "Boost"
    version = "1.64.0"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/Ubitrack/conan-ubitrack"
    description = "TUM CAMPAR Ubitrack Tracking and Sensor Fusion Framework"
    license = "GPL"

    options = {"shared": [True, False],
               "with_default_camera": [True, False],
               "with_network": [True, False],
               "with_python": [True, False],
               "with_tracker_art": [True, False],
               # disabling vision requires more dynamic dependency management in utdataflow/utfacade and deps..
               # "with_vision": [True, False],
               "with_visualization": [True, False],
            }

    default_options = (
        "shared=True",
        "with_default_camera=True",
        "with_network=True",
        # For now we do not want python to be default
        "with_python=False",
        "with_tracker_art=True",
        # "with_vision=True",
        "with_visualization=True",

        # Default settings for dependencies
        # Boost
        "Boost.without_atomic=True",
        "Boost.without_container=True",
        "Boost.without_context=True",
        "Boost.without_coroutine=True",
        "Boost.without_coroutine2=True",
        "Boost.without_exception=True",
        "Boost.without_fiber=True",
        "Boost.without_graph=True",
        "Boost.without_graph_parallel=True",
        "Boost.without_locale=True",
        "Boost.without_log=True",
        "Boost.without_metaparse=True",
        "Boost.without_mpi=True",
        "Boost.without_signals=True",
        "Boost.without_timer=True",
        "Boost.without_type_erasure=True",
        "Boost.without_wave=True"


       )

    requires = (
        "ubitrack_core/1.3.0@ubitrack/stable",
        "ubitrack_component_core/1.3.0@ubitrack/stable",
        "ubitrack_vision/1.3.0@ubitrack/stable",
        "ubitrack_component_vision/1.3.0@ubitrack/stable",
        "ubitrack_dataflow/1.3.0@ubitrack/stable",
        "ubitrack_facade/1.3.0@ubitrack/stable",

        )

    def config_options(self):
        if not self.options.with_vision:
            self.options.remove("with_default_camera")


    def configure(self):
        if self.options.with_python:
            self.options["Boost.with_python"] = True
        else:
            self.options["Boost.with_python"] = False


    def requirements(self):
        if self.options.with_network:
            self.requires("ubitrack_device_comm_zmq/1.3.0@ubitrack/stable")

        if self.options.with_visualization:
            self.requires("ubitrack_visualization/1.3.0@ubitrack/stable")
            self.requires("ubitrack_component_visualization/1.3.0@ubitrack/stable")

        if self.options.with_tracker_art:
            self.requires("ubitrack_device_tracker_art/1.3.0@ubitrack/stable")

        if self.options.with_camera:
            if self.settings.os == "Macos":
                self.requires("ubitrack_device_camera_avfoundation/1.3.0@ubitrack/stable")
            else:
                self.output.warn("No default camera found for OS: %s" % self.settings.os)




