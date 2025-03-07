using OuterSpaceDetection.WebApi.Domain.Dtos;

namespace OuterSpaceDetection.WebApi.Application.Services;

public interface ISpaceObjectClassifier
{
    Task<SpaceObjectDto> ClassifyStarAsync(string imagePath,CancellationToken cancellationToken);
}
