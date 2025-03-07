namespace OuterSpaceDetection.WebApi.Domain.Dtos;

public sealed record SpaceObjectDto(
     string Name,
     double Brightness,
     string Color,
     double Distance);