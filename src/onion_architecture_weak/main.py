from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.iair_quality_service import IAirQualityService
from utils import consts


async def main(
        service: IAirQualityService = Provide[Container.service],
) -> None:
    last_pm10_index = await service.get_air_quality_index(consts.SENSOR_ID)
    mean_pm10_value = await service.get_mean_params(consts.SENSOR_ID)

    print(f"Current AQI: {last_pm10_index}, average PM10 value: {mean_pm10_value}")


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
