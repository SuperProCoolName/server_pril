import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import * as winston from 'winston';
import { loggerConfig } from '../logger/logger.config';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  private logger = winston.createLogger(loggerConfig);

  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const request = context.switchToHttp().getRequest();
    const { method, url, ip, headers, body } = request;
    const userAgent = headers['user-agent'];
    const startTime = Date.now();

    return next.handle().pipe(
      tap((response) => {
        const responseTime = Date.now() - startTime;

        const logMessage = {
          timestamp: new Date().toISOString(),
          method,
          url,
          ip,
          userAgent,
          requestBody: body,
          responseTime: `${responseTime}ms`,
          response: response,
          level: 'info',
        };

        this.logger.info(JSON.stringify(logMessage));
      }),
    );
  }
}
