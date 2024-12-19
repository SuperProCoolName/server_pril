import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { LoggingInterceptor } from './logging/logging.interceptor';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Swagger document configuration
  const config = new DocumentBuilder()
    .setTitle('Recipes API')
    .setVersion('0.1')
    .build();

  // Create a Swagger document using the application instance and the document configuration
  const document = SwaggerModule.createDocument(app, config);

  // Setup Swagger module with the application instance and the Swagger document
  SwaggerModule.setup('api', app, document);
  app.useGlobalInterceptors(new LoggingInterceptor());
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
