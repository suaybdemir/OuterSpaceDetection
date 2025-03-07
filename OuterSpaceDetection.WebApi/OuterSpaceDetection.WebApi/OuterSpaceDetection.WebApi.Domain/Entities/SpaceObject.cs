using OuterSpaceDetection.WebApi.Domain.Abstractions;

namespace OuterSpaceDetection.WebApi.Domain.Entities;

public sealed class SpaceObject : Entity
{
    public string Name { get; set; } = string.Empty;
    public double Brightness { get; set; }
    public string Color { get; set; } = string.Empty;
    public double Distance { get; set; }

}
