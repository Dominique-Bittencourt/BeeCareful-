from code.Raindrop import Raindrop


class RaindropFactory:

    @staticmethod
    def create_from_cloud(screen, cloud):
        x, y = cloud.get_rain_position()

        return Raindrop(
            screen,
            x,
            y,
            cloud
        )

