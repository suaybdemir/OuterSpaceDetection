using Emgu.CV;
using System;

namespace OuterSpaceDetection.WebApi.Application.Services;

public interface IOpenCVService
{
    Task<Mat> ProcessImageAsync(string imagePath,CancellationToken cancellationToken);
}
