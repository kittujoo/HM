import abc


class ManifestCollectorInterface(metaclass=abc.ABCMeta):
    """Interface for enforcing manifest functionality on any environment."""

    @abc.abstractmethod
    def enrich_manifest(self, manifest_dict):
        """Generates manifest file"""
        raise NotImplementedError
