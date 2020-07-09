package com.azure.uploadfile.com.azure.uploadfile;
import com.azure.storage.blob.*;
import com.azure.storage.blob.models.*;
import java.io.*;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
    	String connectStr="DefaultEndpointsProtocol=https;AccountName=upload2017;AccountKey=hRF/4rD/AV/WF3I1srQgHipU0imTKm6nB/4Rk9MwaQlTYPe5AwF1vsfIgow0yb6gYyeTeaKcyzWSeFFQX/DwTQ==;EndpointSuffix=core.windows.net";
    	// Create a local file in the ./data/ directory for uploading and downloading
    //	String localPath = "./data/";
    	String fileName = "NewCars.xlsx";
    	String filePath="/Users/Siddhant/Desktop/Bristlecone/NewCars.xlsx";
    	File localFile = new File(filePath);

    	// Write text to the file
//    	FileWriter writer = new FileWriter(localPath + fileName, true);
//    	writer.write("Hello, World!");
//    	writer.close();
    	// Create a BlobServiceClient object which will be used to create a container client
    	BlobServiceClient blobServiceClient = new BlobServiceClientBuilder().connectionString(connectStr).buildClient();

    	//Create a unique name for the container
    	String containerName = "test2019";

    	// Create the container and return a container client object
    	BlobContainerClient containerClient = blobServiceClient.createBlobContainer(containerName);
    	// Get a reference to a blob
    	BlobClient blobClient = containerClient.getBlobClient(fileName);

    	System.out.println("\nUploading to Blob storage as blob:\n\t" + blobClient.getBlobUrl());

    	// Upload the blob
    	blobClient.uploadFromFile(filePath);
    	System.out.println( "Hello World!" );
        
    }
}
