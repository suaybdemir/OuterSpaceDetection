namespace OuterSpaceDetection.WebApi.Application.Services;

public interface IOpenCVService
{
    Task<string> ProcessImageAsync(string imagePath,CancellationToken cancellationToken);
}
