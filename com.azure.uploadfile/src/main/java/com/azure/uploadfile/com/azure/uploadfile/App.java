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
    	
    	String fileName = "NewCars.xlsx";
    	String filePath="/Users/Siddhant/Desktop/Bristlecone/NewCars.xlsx";
    	File localFile = new File(filePath);

    	
    	BlobServiceClient blobServiceClient = new BlobServiceClientBuilder().connectionString(connectStr).buildClient();

    	
    	String containerName = "test2019";

    	
    	BlobContainerClient containerClient = blobServiceClient.createBlobContainer(containerName);
    	
    	BlobClient blobClient = containerClient.getBlobClient(fileName);

    	

    	
    	blobClient.uploadFromFile(filePath);
    	
        
    }
}
