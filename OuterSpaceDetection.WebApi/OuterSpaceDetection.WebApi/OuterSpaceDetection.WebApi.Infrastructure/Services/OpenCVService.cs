using Microsoft.AspNetCore.Http.HttpResults;
using OuterSpaceDetection.WebApi.Application.Services;
using System.Drawing;

namespace OuterSpaceDetection.WebApi.Infrastructure.Services;

public sealed class OpenCVService : IOpenCVService
{
    public async Task<string> ProcessImageAsync(string imagePath, CancellationToken cancellationToken)
    {
        byte[] imageBytes = File.ReadAllBytes(imagePath);
        string base64String = Convert.ToBase64String(imageBytes);

        // It sent image to OpenCV service and get result

        return await Task.Run(() => "Image processed successfully");
    }
}
