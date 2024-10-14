from dependency_injector import containers, providers

from repositories.air_quality_repository import AirQualityRepository
from services.air_quality_service import AirQualityService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repository = providers.Singleton(
        AirQualityRepository,
    )

    service = providers.Factory(
        AirQualityService,
        repository=repository,
    )
