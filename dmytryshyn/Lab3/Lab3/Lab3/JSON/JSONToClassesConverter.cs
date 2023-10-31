using Lab3.Classes.Ships;
using Lab3.DTO;
using MySecondPattern.Classes.Containers;
using MySecondPattern.Classes.Containers.Abstractions;
using MySecondPattern.Classes.Ports;
using MySecondPattern.Classes.Ships;
using Newtonsoft.Json;
using System.Reflection;
using static System.Net.Mime.MediaTypeNames;

namespace Lab3.JSON
{
    public static class JSONToClassesConverter
    {
        public static string currentDirectory = Directory.GetCurrentDirectory();
        public static string jsonFileFolderName = "Lab3\\JSON\\Files";

        public static List<Container> CreateContainers()
        {
            string jsonString = File
                .ReadAllText(getFilePath("Containers"));

            return JsonConvert
                .DeserializeObject<List<ContainerDTO>>(jsonString)
                .Select(i => ContainerCreationStrategy.CreateContainer(i.Id,i.Weight,i.Type))
                .ToList();            
        }

        public static List<Port> CreatePorts()
        {

            string jsonString = File
                .ReadAllText(getFilePath("Ports"));

            return JsonConvert
                .DeserializeObject<List<PortDTO>>(jsonString)
                .Select(i => new Port(i.Id,i.Latitude,i.Longitude))
                .ToList();
        }

        public static List<Ship> CreateShips()
        {
            string jsonString = File
                .ReadAllText(getFilePath("Ships"));

            return JsonConvert
                .DeserializeObject<List<ShipDTO>>(jsonString)
                .Select(i => ShipFactory
                    .CreateShip(i.ShipTypes, i.Id, i.ShipLimitsCharacteristics, i.Fuel))
                .ToList();
        }



        private static string getFilePath(string itemType)
        {
            string containerFileName = $"{itemType}.json";
            string mainDirectoryPath = getMainDirectory();
            return Path.Combine(mainDirectoryPath, jsonFileFolderName, containerFileName);
        }

        private static string getMainDirectory()
        {
            string directory = currentDirectory;
            for (int i = 0; i < 2; i++)
            {
                directory = Directory
                    .GetParent(directory)
                    .Parent
                    .FullName;
            };

            return directory;
        }

    }
}
